SPAM_FILE = './data/spam.txt'

def read_file(filename): 
	data = ""
	with open(filename) as file: 
		data = file.readlines() 
	return data

def train_spam(training_data): 
	

if __name__ == '__main__':
	data = [line.strip() for line in read_file(SPAM_FILE)] 
	print(data)

