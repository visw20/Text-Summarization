from transformers import BartForConditionalGeneration, BartTokenizer

# Load pre-trained model and tokenizer
model_name ='facebook/bart-large-cnn'
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

while True:
  # Get user input
  text = input("Enter text to be summarized (or 'q' to quit): ")

  # Check for quit command
  if text.lower() == 'q':
    break

  # Summarize text
  inputs = tokenizer(text, max_length=1024, return_tensors='pt', truncation=True)
  summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
  summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

  # Print summary
  print(summary)

  # Ask to continue
  continue_summarizing = input("Summarize another text (y/n)? ")
  if continue_summarizing.lower() != 'y':
    break

print("Summary generation stopped.")