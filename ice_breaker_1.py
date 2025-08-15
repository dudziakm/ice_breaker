from dotenv import load_dotenv
import os
if __name__ == '__main__':
    load_dotenv()
    print('Hello LangChain\n')
    print(os.environ['COOL_API_KEY'])