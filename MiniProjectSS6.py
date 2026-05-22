quantity_laptop = 0
quantity_phone = 0
quantity_tablet = 0 

while True:
    choose = int(input("=== MENU === \n" 
                "1. Xem báo cáo tồn kho \n" 
                "2. Nhập kho \n"
                "3. Xuất kho \n"
                "4. Cảnh báo tồn kho thấp \n"
                "5. Thoát chương trình \n"
                "Nhập lựa chọn: "))
    if choose == 1:
        print(f"Laptop({quantity_laptop}): {"*" * quantity_laptop}")
        print(f"Phone({quantity_phone}): {"*" * quantity_phone}")
        print(f"Tablet({quantity_tablet}): {"*" * quantity_tablet}")
    elif choose == 2:
        category_product = int(input("1-Laptop, 2-Phone, 3-Tablet \n"
                                        "Chọn sản phẩm"))
        add_product = int(input("Nhập số sản phẩm cần thêm: "))
        while add_product < 0:
            print("Số lượng không hợp lệ, vui lòng nhập lại: ")
            add_product = int(input("Nhập số sản phẩm cần thêm: "))
        match category_product:
            case 1: 
                quantity_laptop += add_product
            case 2:
                quantity_phone += add_product
            case 3:
                quantity_tablet += add_product  
            case _: 
                print("Lựa chọn không hợp lệ")
    elif choose == 3:
        category_product = int(input("1-Laptop, 2-Phone, 3-Tablet \n"
                                        "Chọn sản phẩm"))
        warehouse = int(input("Nhập số lượng xuất kho"))
        while warehouse < 0:
            print("Số lượng không hợp lệ, vui lòng nhập lại: ")
            warehouse = int(input("Nhập số lượng xuất kho"))
        match category_product:
            case 1: 
                if warehouse <= quantity_laptop:
                    quantity_laptop -= warehouse
                else: 
                    print("Không đủ hàng")
            case 2:
                if warehouse <= quantity_phone:
                    quantity_phone -= warehouse
                else: 
                    print("Không đủ hàng")
            case 3:
                if warehouse <= quantity_tablet:
                    quantity_tablet -= warehouse
                else: 
                    print("Không đủ hàng") 
            case _: 
                print("Lựa chọn không hợp lệ")
    elif choose == 4:
        if quantity_laptop < 10:
            print("Mặt hàng laptop sắp hết")
        if quantity_phone < 10:
            print("Mặt hàng phone sắp hết")
        if quantity_tablet < 10:
            print("Mặt hàng tablet sắp hết")
    elif choose == 5:
        break
    else: 
        print("Lựa chọn không hợp lệ")