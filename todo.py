fulltaskList = []
# Function to add tasks
def addTask():
  user_input = input('Enter the tasks for today (separated by commas): ')
  tasks = user_input.split(',')  # Split input into a list
  for task in tasks:
      fulltaskList.append(task.strip())
  
  print("\n📋 Here is your updated task list:")
  for task in fulltaskList:
      print(f"- {task}")
# Function to view tasks
def viewTask():
  if len(fulltaskList) > 0:
      print('\n📋 View Tasks:')
      for item in fulltaskList:
          print(f"- {item}")
  else:
      print('\n⚠️ No items to view.')
# Function to delete all tasks
def deleteTask():
  if len(fulltaskList) > 0:
      fulltaskList.clear()
      print('\n🧹 To-Do list is now empty.')
  else:
      print('\n⚠️ List is already empty.')
# Main input block
action_input = input('\nWhat task do you want to perform? (add / view / delete): ').lower()
if action_input == 'add':
  addTask()
elif action_input == 'view':
  viewTask()
elif action_input == 'delete':
  deleteTask()
else:
  print("❌ Invalid input. Please type: add, view, or delete.")
