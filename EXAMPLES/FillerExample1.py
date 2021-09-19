from IdaiKuri.Filler import FillerTemplateEngine as TemplateEngine
from IdaiKuri.Filler import Interface

TE = TemplateEngine();
TE.InFile("TemplateFiles/Template_DefaultCase1.html", True); 
temp_vars = TE.VARS();

temp_vars.Portrait = "images/GuidoVanRossum.png";
temp_vars.Logo = "images/PythonLogo.png";
temp_vars.FullName = "Guido Van Rossum";
temp_vars.Position = "Python's Benevolent Dictator for life";
temp_vars.Quote = "In Python, every symbol you type is essential.";
temp_vars.Author = "Guido van Rossum";
result_dict = TE.OutFile(temp_vars, "GeneratedFiles/GuidoVanRossum_DefaultCase1.html");