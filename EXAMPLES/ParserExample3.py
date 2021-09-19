from IdaiKuri.Parser import ParserTemplateEngine as TemplateEngine

PE = TemplateEngine(("<<", ">>"), "<<self.FUNC_CALL()>>");
print("\n", "Template_SpecialCase2.html", "GuidoVanRossum_SpecialCase2.html", "\n");
diffdict = PE.Root("TemplateFiles/Template_SpecialCase2.html", "GeneratedFiles/GuidoVanRossum_SpecialCase2.html");
for key in diffdict.keys():
    print("   ", key, "->", diffdict[key]);