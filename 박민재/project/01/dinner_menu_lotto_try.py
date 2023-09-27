from menu import *
from soup import *
from side_dish import *

intro_menu = """랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
식단짜기 : 6
종료하기 : 7\n"""
return_menu = "반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    식단짜기 >> 6   종료하기 >> 7"
failed_menu = "팔지 않는 메뉴입니다. 다시 입력해 주세요!"
error_message = "맞지 않은 번호입니다! 다시 입력해 주세요!"
menu_dict_1 = {
    1: print_gal,
    3: print_gogalby,
    5: print_cucumber_muchim,
    7: print_pork_neck,
    9: print_lettuce_kimchi,
    11: print_braised_tofu,
    13: print_braised_radish_with_mackerel
}
menu_dict_2 = {
    2: print_JJagle,
    4: print_Perilla_Kimchi,
    6: print_Seaweed_Soup,
    8: print_Beef_Bone_Soup,
    10: print_Soybean_Sprout_Soup
}
menu_dict = menu_dict_1.copy()
menu_dict.update(menu_dict_2)
print(intro_menu)
while True:  # 무한 반복(현업에선 거의 안 씀. 메모리 뻑나서)
    try:
        dinner = int(input(""))
        import random  # 랜덤한 숫자 뽑아내기

        random_number_1 = random.randint(1, 9)
        random_number_2 = random.randint(1, 9)
        if dinner == 1:  # 1 입력시 랜덤한 숫자 출력 후 문장 출력 및 처음으로 돌아감
            print(f"{random_number_1}\n{return_menu}")
        elif dinner == 2:  # 2 입력시 랜덤한 숫자 두개 출력 후 문장 출력 및 처음으로 돌아감
            print(f"( {random_number_1} / {random_number_2} )\n{return_menu}")
        elif dinner == 3:  # 3 입력시 반찬 메뉴판 출력
            print_side_dish()
            food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
            if food == 0:  # 처음 안내판 출력
                print(intro_menu)
            elif food in menu_dict_1:  # 출력한 메뉴판에서 원하는 음식에 해당하는 번호 입력 시 해당 레시피 출력
                print(menu_dict_1[food])
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
                print(failed_menu + "\n" + return_menu)
        elif dinner == 4:  # 4 입력시 국 메뉴판 출력
            print_soup()
            food = int(input("원하시는 국의 번호를 선택해주세요\n"))
            if food == 0:  # 처음 안내판 출력
                print(intro_menu)
            elif food in menu_dict_2:  # 출력한 메뉴판에서 우너하는 음식에 해당하는 번호 입력 시 해당 레시피 출력
                print(menu_dict_2[food])
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
                print(failed_menu + "\n" + return_menu)
        elif dinner == 5:  # 5 입력시 전체 메뉴판 출력
            print_menu()
            food = int(input("\n메뉴의 번호를 입력하세요!\n"))
            if food == 0:  # 0 입력시 intro_menu 호출 후 26번줄로 돌아감
                print(intro_menu)
            elif food in menu_dict:  # 1 입력 후 숫자에 해당하는 레시피 출력 후 26번줄로 돌아감
                print(menu_dict[food])
                print(return_menu)
            else:  # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
                print(failed_menu + "\n" + return_menu)
        elif dinner == 6:
            list_a = [512, 356, 477, 611, 532, 453, 499, 378, 561, 444, 531, 601, 387, 426, 468]
            list_b = [95, 142, 111, 132, 128, 89, 121, 99, 104, 71, 101, 130, 95, 108, 102]

            result_a = []
            result_b = []
            total_sum = 0

            while True:
                if len(result_a) == 7 and len(result_b) == 7:
                    break
                selected_list = random.choice([list_a, list_b])
                selected_number = random.choice(selected_list)
                if selected_list is list_a and len(result_a) < 7 and 4000 <= total_sum + selected_number <= 5000:
                    result_a.append(selected_number)
                    total_sum += selected_number
                elif selected_list is list_b and len(result_b) < 7 and 4000 <= total_sum + selected_number <= 5000:
                    result_b.append(selected_number)
                    total_sum += selected_number
            print("랜덤하게 선택된 반찬의 칼로리:", result_a)
            print("랜덤하게 선택된 국의 칼로리:", result_b)
            print("반찬 칼로리의 총합:", sum(result_a))
            print("국 칼로리의 총합:", sum(result_b))
            print("총합:", total_sum)
            print(return_menu)
        elif dinner == 7:  # 6 입력시 종료
            print("장비를 정지합니다.")
            break
        else:
            if dinner >= 8:  # 7 이상의 숫자 입력시 에러 출력 후 되돌아가기
                raise ValueError(error_message + "\n" + return_menu)
            print(error_message + "\n" + return_menu)
    except ValueError:
        print(error_message + "\n" + return_menu)

# if/elif 구조를 try로 바꾸기
# class 선언으로 간소하하기 def 메뉴, 밥, 국
# 콜백과 1급함수 공부해서 메모리 주소 나오는거 고치기
# 디버깅툴로 코드 흐름 따라가기
