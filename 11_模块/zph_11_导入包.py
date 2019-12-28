import zph_message

zph_message.send_message.send("hello")

receive_text = zph_message.receive_message.receive()

print(receive_text)