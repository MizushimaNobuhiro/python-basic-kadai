def commodity_total(price, tax):
  tax_total = price * tax / 100
  commodity_total = price + tax_total
  print(f"{price}円(税込：{commodity_total}円)")
  
commodity_total(800, 10)