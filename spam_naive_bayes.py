SPAM_FILE = './data/spam.txt'
NOT_SPAM = 'ham'
SPAM = 'spam'
TAB_CODE = '\t'


def read_file(filename): 
	data = ""
	with open(filename) as file: 
		data = file.readlines() 
	return data

def get_body_text(training_data): 
	return [line.split(TAB_CODE)[1] for line in training_data]

def train_spam(training_data): 
	total_lines = 0
	spam_count = 0

	for line in training_data: 
		if line.startswith(SPAM): 
			spam_count += 1

	p_spam = float(spam_count) / total_lines
	p_not_spam = float(total_lines - spam_count) / total_lines

	return p_spam, p_not_spam


if __name__ == '__main__':
	data = [line.strip() for line in read_file(SPAM_FILE)] 
	print(data)



