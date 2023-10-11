# Load model directly
from transformers import AutoTokenizer, AutoModelForPreTraining

tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-v3").save_pretrained("./bert/bert-base-japanese-v3")
model = AutoModelForPreTraining.from_pretrained("cl-tohoku/bert-base-japanese-v3").save_pretrained("./bert/bert-base-japanese-v3")