import pandas as pd
from src.handlers import TextHandler


class DataHandler:
    def __init__(self) -> None:
        text_handler = TextHandler()

    def clean_csv(self, file_path):
        df = pd.read_csv(file_path)
        
        # Remove undesired attributes
        self.remove_terms(['__link__', 'RT :'], df)
        self.remove_regex(['@\w+'], df)
        self.remove_accent_marks(df)
        df = self.remove_duplicated_text(df)
        
        # Extract desired attributes
        df['hashtags'] = df.text.str.findall('#\w+')
        self.remove_regex(['#\w+'], df)

        # Remove remaining artifacts
        df.text = df.text.str.extract('(\w.*)')
        df.text = df.text.str.replace('#', '')
        df.text = df.text.str.strip()
        df.text = df.text.str.capitalize()
        


    def remove_terms(self, terms, df):
        for term in terms:
            df.text = df.text.str.replace(term,'', regex = False)

    
    def remove_regex(self, terms, df):
        for term in terms:
            df.text = df.text.str.replace(term,'',regex = True)

    
    def remove_accent_marks(self, df):
        df.text = df.text.str.encode('ascii', errors='ignore').str.decode('utf-8')

    def remove_duplicated_text(self, df):
        df = df.groupby('text').first().reset_index()
        return df