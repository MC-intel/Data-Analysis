import random
import pandas as pd

topic = ['action','horror','romance']
personal = []

data = []

while True:
    A = random.choice(topic)
    print(A)
    print('Continue watching?')
    print('yes no or never')

    u_input = input()
    if 'yes' in u_input.lower():
        personal.append(A)
        topic.extend(personal)
        data.append((A, "yes"))
        print(topic)
    elif 'no' in u_input.lower():
        data.append((A, "no"))
        print('sorry')
    elif 'never' in u_input.lower():
        topic.remove(A)
        data.append((A, "never"))
        print(topic)
    else:
        break

df = pd.DataFrame(data, columns=["topic", "response"])
print(df)


#C++

#include <iostream>
#include <string>
#include <vector>
#include <random>

std::vector<std::string> topic = {"action", "horror", "romance"};

int main() {
  std::vector<std::string> personal;
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis(0, topic.size() - 1);

  while (true) {
    std::string A = topic[dis(gen)];
    std::cout << A << std::endl;
    std::cout << "Continue watching?" << std::endl;
    std::cout << "yes no or never" << std::endl;

    std::string u_input;
    std::cin >> u_input;
    std::transform(u_input.begin(), u_input.end(), u_input.begin(), ::tolower);
    if (u_input == "yes") {
      personal.push_back(A);
      topic.insert(topic.end(), personal.begin(), personal.end());
      std::cout << topic << std::endl;
    } else if (u_input == "no") {
      std::cout << "sorry" << std::endl;
    } else if (u_input == "never") {
      topic.erase(std::remove(topic.begin(), topic.end(), A), topic.end());
      std::cout << topic << std::endl;
    } else {
      break;
    }
  }

  return 0;
}


