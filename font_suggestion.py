import requests
import pandas as pd

class FontSuggestion:
    """
    Class is used to find font according to your style.
    """

    def __init__(self) -> None:
        self.base_url = "https://webfonts.googleapis.com/v1/webfonts"
        self.api_key = "AIzaSyCOaMduvF9xRvsJGXJbAiMhN_fTBUUv0Lg"
        self.prompt = None
    
    def req(self) -> tuple:
        """
        Function is used get the dataset from google font api.

        params:
            None
        
        return:
            tuple: condition, result
        """

        try:
            base = self.base_url + "?key=" + self.api_key
            response = requests.get(base)
            return True, response.json()
        except Exception as e:
            return False, e
        
    def find_style(self, prompt):
        """
        Function is used to search and filter the fonts according to the prompt.

        params:
            prompt: (string) weight value
        
        return:
            tuple: condition, dataframe
        """
        self.prompt = prompt.lower()
        cond, fonts = self.req()

        result = []
        if cond:
            if self.prompt == "thin":
                for item in fonts.get("items"):
                    # if len(result) >= 10:
                    #     break
                    exists = False
                    for variant in item.get("variants"):
                        if "100" in variant:
                            exists = True
                        elif "200" in variant:
                            exists = True
                        elif "300" in variant:
                            exists = True
                    if exists:
                        result.append(item)

            elif self.prompt == "regular":
                for item in fonts.get("items"):
                    # if len(result) >= 10:
                    #     break
                    exists = False
                    for variant in item.get("variants"):
                        if "regular" in variant:
                            exists = True
                    if exists:
                        result.append(item)

            elif self.prompt == "bold":
                for item in fonts.get("items"):
                    # if len(result) >= 10:
                    #     break
                    exists = False
                    for variant in item.get("variants"):
                        if "500" in variant:
                            exists = True
                        elif "600" in variant:
                            exists = True
                        elif "700" in variant:
                            exists = True
                        elif "800" in variant:
                            exists = True
                        elif "900" in variant:
                            exists = True
                    if exists:
                        result.append(item)

            df = pd.DataFrame(result)

            return True, df
        else:
            return False, "Error occured while getting fonts!"
            

if __name__ == "__main__":
    font_suggestion = FontSuggestion()
    result = font_suggestion.find_style("thin")
    print(result)

    # import json

    # with open("fonts.json", "w") as f:
    #     json.dump(fonts, f)    