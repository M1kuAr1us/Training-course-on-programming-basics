import ast
import dis

code = "print (\"Hello World\")"
func = ("print (\"Hello World \", \"ABC\")")
tree = ast.parse(code)
print(ast.dump(tree, indent=4),"\n")

print(compile("print (\"Hello World\")", "", "eval").co_code,"\n")

dis.dis(b'\x97\x00\x02\x00\x65\x00\x64\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x53\x00')
print("\n")
dis.dis(compile("print (\"Hello World\")", "", "eval").co_code)
print("\n")

print(compile("print (\"Hello World\")", "", "eval").co_consts,"\n")

dis.dis(compile(func, "", "exec"))