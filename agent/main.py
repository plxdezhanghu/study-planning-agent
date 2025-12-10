from agent.input_handler import collect_user_input
from agent.planner import generate_plan


def main():
    """
    程序入口：负责循环交互，不写业务细节。
    """
    while True:
        user_info = collect_user_input()
        result = generate_plan(user_info)

        print("\n===== 学习计划 =====\n")
        print(result)
        print("\n====================\n")

        cont = input("是否再生成一份计划？(y/n)\n> ").strip().lower()
        if cont != "y":
            print("好的，今天就到这里，继续加油！")
            break


if __name__ == "__main__":
    main()
