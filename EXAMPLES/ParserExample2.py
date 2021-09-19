from IdaiKuri.Parser import ParserTemplateEngine as TemplateEngine

PE = TemplateEngine();
print("\n", "Template_DefaultCase2.html", "GuidoVanRossum_DefaultCase2.html", "\n");
diffdict = PE.Root("TemplateFiles/Template_DefaultCase2.html", "GeneratedFiles/GuidoVanRossum_DefaultCase2.html");
for key in diffdict.keys():
    print("   ", key, "->", diffdict[key]);