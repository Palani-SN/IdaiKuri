from IdaiKuri.Parser import ParserTemplateEngine as TemplateEngine

PE = TemplateEngine();
print("\n", "Template_DefaultCase1.html", "GuidoVanRossum_DefaultCase1.html", "\n");
diffdict = PE.Root("TemplateFiles/Template_DefaultCase1.html", "GeneratedFiles/GuidoVanRossum_DefaultCase1.html");
for key in diffdict.keys():
    print("   ", key, "->", diffdict[key]);