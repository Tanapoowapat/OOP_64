from Agent import Agent
agent_list = []

print("Welcome to Property Programe")
def main():
    while True:
        print("="*30)
        print("1.Create Agent\n2.Show Agent")
        print("="*30)
        command_option = int(input("Select Menu : "))
        if command_option == 1:
            name = input("Enter Agent Name : ").lower()
            agent = Agent(name)
            agent_list.append(agent)
            
        elif command_option == 2:
            for agent in agent_list:
                print(agent.name)
            select_agent = input("Select Agent : ").lower()
            for agent in agent_list:
                if select_agent == agent.name:
                    agent_menu(agent)
                else:
                    print('Agent Not Found')

def agent_menu(select_agent):

    print("="*30)
    print("Agent Menu")
    print("="*30)
    
    while True:
        print(f'Agent Name : {select_agent.name}')
        print("="*30)
        print("1.Add Property\n2.Show Property\n3.Exit this Agent Menu")
        print("="*30)
        option = int(input("Select Menu : "))
        if option == 1:
            select_agent.add_property()

        elif option == 2:
            print("="*30)
            print("1.Show All Property\n2.Select Property")
            select_show = int(input("Select Menu : "))
            print("="*30)
            if select_show == 1 :
                select_agent.list_property(True)
            if select_show == 2 :
                select_agent.list_property(False)
        elif option == 3:
            main()
        else :
            print("Invalid input")

main()