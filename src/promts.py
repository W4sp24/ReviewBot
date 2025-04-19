
class BloomTaxonomy:
    
    @staticmethod
    def remembering(topic):
        prompt = f"Using Bloom’s Taxonomy Level 1 (Remembering), extract key terms and their definitions from the following text. Each term should be separated with a hyphen followed by its definition. Remove asterisk and make sure the output is clean and neat. Definition must be simple and avoid using capitalization to highlight words, while adhering to proper sentence structures: {topic}"
        return prompt


    
