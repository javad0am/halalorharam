import google.generativeai as genai

genai.configure(api_key="")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "گوشت خر حلاه یا حرام است در اسلام؟",
      ],
    },
    {
      "role": "model",
      "parts": [
        "گوشت خر در اسلام حرام است.  به طور کلی، حیواناتى که گوشت آنها حلال نیست در اسلام، شامل حیواناتى است که در شریعت اسلامی شرایط لازم را برای حلال بودن گوشت آن ها دارا نیستند.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "از الان به بعد اسم هر خوراکی رو گفتم حلال بود فقط و فقط بگو 1 اگه حرام بود فقط بگو 0",
      ],
    },
    {
      "role": "model",
      "parts": [
        "1\n",
      ],
    },
  ]
)


while True:
  INS = input('خوراک را وارد کنید:   ')

  response = chat_session.send_message(INS)

  # تبدیل پاسخ به عدد و حذف فضاهای خالی
  response_value = int(response.text.strip())

  if response_value == 1:
    print('\nحلال است...')
  elif response_value == 0:
    print('\nحلال نیست...')
  else:
    print('ارور ناشناخته')