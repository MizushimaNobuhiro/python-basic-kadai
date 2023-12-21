def commodity_total(price, tax):
  tax = price * 0.1
  commodity_total = price + tax
  print(f"{price}円(税込：{commodity_total}円)")
  
commodity_total(800, 10)