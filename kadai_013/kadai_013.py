def commodity_total(price, tax):
  commodity_total = price * tax
  print(f"{price}円(税込：{commodity_total}円)")
  
commodity_total(800, 1.1)