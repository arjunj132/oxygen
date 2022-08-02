# Lexer and Parser of the Oxygen Programming Language
# Designed for Nitrogen
# (c) Arjun J

import sys
import json
import os

class Oxygen:
    def __init__(self, code):
        self.code = code
    def lexer(self):
        code = self.code
        length = len(code)
        pos = 0
        tokens = []
        custom_keywords = []
        BUILT_IN_KEYWORDS = ["print", "function", "import"]
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_()""\','
        mathoperators = '+-/*%'
        allowedfunc = []
        allowedkey = []
        while pos < length:
            currentchar = code[pos]
            if currentchar == " " or currentchar == '\n':
                pos += 1
                pass
            elif currentchar == '"':
                res = ""
                pos += 1
                while code[pos] != '"' and code[pos] != '\n' and pos < length:
                    res += code[pos]
                    pos += 1
                if code[pos] != '"':
                    return {
                        "error": "String does not end with \"" 
                    }
                pos += 1

                tokens.append({
                    "type": "string",
                    "value": res
                })
            elif currentchar in chars:
                res = currentchar
                pos += 1
                while code[pos] in chars + "1234567890" and pos < length:
                    res += code[pos]
                    pos += 1
                if res not in BUILT_IN_KEYWORDS:
                    
                    if tokens[len(tokens) - 1]["value"] != "function":
                        if res not in allowedfunc:
                            
                            works = False
                            for x in allowedkey:
                                if res.split("(")[0] + "(" in x:
                                    works = True
                            if res == ")":
                                works = True
                            
                            if works == False:
                                return {
                                    "error": 'Unexpected token "%s"' % res
                                }
                            else:
                                tokens.append({
                                    "type": "run",
                                    "value": res
                                })
                                
                                

                        else:
                            if res in allowedfunc and res in allowedkey:
                                print("Function and module both have the same value")
                            elif res in allowedfunc:
                                tokens.append({
                                    "type": "functioncalled",
                                    "value": res
                                })
                            else:
                                for x in allowedkey:
                                    if res.split("(")[0] + "(" in x:
                                        tokens.append({
                                            "type": "run",
                                            "value": res
                                        })
                            
                    else:
                        tokens.append({
                            "type": "funcname",
                            "value": res
                        })
                        
                        allowedfunc.append(res)
                        
                        try:
                            if code[pos + 1] == " ":
                                pos += 1
                        except:
                            pass
                        
                        pos += 1
                        
                        res = ""
                        
                        try:
                            while code[pos] != ":" and pos < length:
                                res += code[pos]
                                pos += 1
                        except:
                            return {
                                "error": "Expected \":\""
                            }
                        
                        
                        pos += 1
                        
                        tokens.append({
                            "type": "funcdef",
                            "value": res
                        })
                else:
                    tokens.append({
                        "type": "keyword",
                        "value": res
                    })
                    
                    if res == "import":
                        try:
                            if os.getcwd().split("/")[-1] != "workspace":
                                os.chdir("workspace")
                            os.chdir("../")
                            res = ""
                            if code[pos + 1] == " ":
                                pos += 1
                            pos += 2
                            while code[pos] != '"' and code[pos] != '\n' and pos < length:
                                res += code[pos]
                                pos += 1
                            checkmodulecommands = open("opl/" + res + "/commands.json")
                            x = checkmodulecommands.read()
                            y = json.loads(x)
                            for z in y:
                                allowedkey.append(z)
                            tokens.append({
                                "type": "importdef",
                                "value": res
                            })
                            pos +=1
                        except:
                            return {
                                "error": "Could not import module"
                            }
                    
            elif currentchar in mathoperators:
                tokens.append({
                    "type": "op",
                    "value": currentchar
                })
                pos+=1
            elif currentchar in "1234567890":
                res = currentchar
                
                pos += 1
                while code[pos] in "1234567890." and pos < length:
                    res += code[pos]
                    pos += 1
                
                tokens.append({
                    "type": "num",
                    "value": float(res)
                })
            else:
                return {
                    "error": 'Unexpected character "%s"' % code[pos]
                }
          

        return {
            "error": False,
            "tokens": tokens
        }
    
    def parse(self, tokens):
        customfunc = []
        functionvalue = []
        imports = []
        commands = []
        length = len(tokens)
        pos = 0
        while pos < length:
            token = tokens[pos]
            
            if token['type'] == "keyword" and token['value'] == "print":
                try:
                    if tokens[pos + 1]:
                        pass
                except:
                    print("Unexpected end of line, expected string")
                    sys.exit()
                    
                isString = tokens[pos + 1]['type'] == "string"
                if (isString == False):
                    print("Unexpected token \"" + tokens[pos + 1]['value'] + "\", expected string")
                    sys.exit()
                
                print(tokens[pos + 1]['value'])
                pos += 2
            elif token["type"] == "op":
                try:
                    if tokens[pos - 1]["type"] != "string" and tokens[pos - 1]["type"] != "num":
                        print("Expected type string or num, not " + tokens[pos - 1]["type"])
                        sys.exit()
                    else:
                        if tokens[pos + 1]["type"] != tokens[pos - 1]["type"]:
                            print("Expected type " + tokens[pos - 1]["type"] + ", not " + tokens[pos + 1]["type"])
                            sys.exit()
                        else:
                            if tokens[pos + 1]["type"] == "string" and token["value"] != "+":
                                print("Cannot perform operation, string can only perform \"+\"")
                                sys.exit()
                            else:
                                if tokens[pos + 1]["type"] == "string":
                                    res = tokens[pos - 1]["value"] + tokens[pos + 1]["value"]
                                    print(res)
                                else:
                                    operation = token["value"]
                                    if operation == "+":
                                        print(tokens[pos - 1]["value"] + tokens[pos + 1]["value"])
                                    if operation == "-":
                                        print(tokens[pos - 1]["value"] - tokens[pos + 1]["value"])
                                    if operation == "*":
                                        print(tokens[pos - 1]["value"] * tokens[pos + 1]["value"])
                                    if operation == "/":
                                        print(tokens[pos - 1]["value"] / tokens[pos + 1]["value"])
                                    if operation == "%":
                                        print(tokens[pos - 1]["value"] % tokens[pos + 1]["value"])
                                pos += 2
                except:
                    print("Can not find one of the one of the arguments required for performing the operation")
                    sys.exit()
            elif token["type"] == "keyword" and token["value"] == "function":
                if tokens[pos + 1]["type"] != "funcname":
                    print("Expected a function name, but instead got a " + tokens[pos + 1]["type"])
                    sys.exit()
                customfunc.append(tokens[pos + 1]["value"])
                pos += 2
            elif token["type"] == "funcdef":
                functionvalue.append(token["value"])
                pos += 1
            elif token["value"] in customfunc and token["type"] == "functioncalled":
                self.code = "\n" + functionvalue[customfunc.index(token["value"])] + "\n"
                self.parse(self.lexer()["tokens"])
                pos += 1
            elif token["type"] == "keyword" and token["value"] == "import":
                if tokens[pos + 1]["type"] != "importdef":
                    print("Expected type importdef, but instead got " + tokens[pos + 1]["type"])
                    sys.exit()
                pos += 1
            elif token["type"] == "importdef":
                imports.append(token["value"])
                checkmodulecommands = open("opl/" + token["value"] + "/commands.json")
                x = checkmodulecommands.read()
                y = json.loads(x)
                for z in y:
                    commands.append(z)
                pos += 1
            elif token["type"] == "run":
                exec("from opl." + imports[commands.index(token["value"].split("(")[0] + "()")] + ".run import *\n" + token["value"], globals(), locals())
                pos += 1
            elif token["type"] == "string":
                pass
                pos += 1
            elif token["type"] == "num":
                try:
                    if tokens[pos + 1]["type"] == "op":
                        pass
                    else:
                        print(token["value"])
                except:
                    print(token["value"])
                pos += 1
            else:
                print("Unexpected token " + token["type"])
                sys.exit()