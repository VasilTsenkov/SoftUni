room_rent = int(input())

price_statue = room_rent * 0.70
price_catering = price_statue * 0.85
price_audio = price_catering * 0.5
total_price = room_rent + price_statue \
              + price_catering + price_audio

print(f'{total_price:.2f}')
