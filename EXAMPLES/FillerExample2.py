from IdaiKuri.Filler import FillerTemplateEngine as TemplateEngine
from IdaiKuri.Filler import Interface

class AdvancedTemplate(TemplateEngine):

    @Interface
    def get_portrait(self, name):

        return "images/"+name.replace(" ","")+".png";

    @Interface
    def get_logo(self, contrib):

        return "images/"+contrib+"Logo.png"
        
TE = AdvancedTemplate();
TE.InFile("TemplateFiles/Template_DefaultCase2.html", True); 
temp_vars = TE.VARS();

temp_vars = TE.VARS();
temp_vars.FullName = "Guido Van Rossum";
temp_vars.Position = "Python's Benevolent Dictator for life";
temp_vars.Quote = "In Python, every symbol you type is essential.";
temp_vars.Contribution = "Python"
result_dict = TE.OutFile(temp_vars, "GeneratedFiles/GuidoVanRossum_DefaultCase2.html");