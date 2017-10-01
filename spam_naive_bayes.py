SPAM_FILE = './data/spam.txt'
NOT_SPAM = 'ham'
SPAM = 'spam'
TAB_CODE = '\t'
ALPHA = 1 


def read_file(filename): 
	data = ""
	with open(filename) as file: 
		data = file.readlines() 
	return data


def process_msg(msg, spam_dict, ham_dict, positive_count, negative_count): 
	isSpam, msg_txt = msg.split(TAB_CODE)
	words = msg_txt.split()

	for word in words: 
		count = 0
		if isSpam == SPAM: 
			count = spam_dict.get(word, 0) + 1
			spam_dict[word] = count
			positive_count[0] += 1 

		else: 
			count = ham_dict.get(word, 0) + 1
			ham_dict[word] = count
			negative_count[0] += 1


def get_word_cond_p(word, word_dict, total_count): 
	num_words = len(word_dict.keys())
	return (word_dict.get(word, 0) + ALPHA) / (total_count + ALPHA * num_words)


def train_spam(training_data): 
	total_lines = len(training_data)
	spam_count = 0

	words_spam = {} # frequency dict of words in spam
	words_ham = {} # frequency dict of words not in spam
	pos_count = [0] # number of words that are spam
	neg_count = [0] # number of words that are not spam

	for line in training_data: 
		if line.startswith(SPAM): 
			spam_count += 1
		process_msg(line, words_spam, words_ham, pos_count, neg_count)

	p_spam = float(spam_count) / total_lines
	p_not_spam = float(total_lines - spam_count) / total_lines

	return p_spam, p_not_spam, words_spam, words_ham, pos_count[0], neg_count[0]


def get_email_cond_p(msg, cond_prob_dict, total_count): 
	text = msg.strip().split()
	result = 1

	for word in text: 
		result *= get_word_cond_p(word, cond_prob_dict, total_count)

	return result

def get_prob_predictions(msg, words_spam, words_ham, p_spam, p_ham): 

	prediction_spam = p_spam * get_email_cond_p(msg, words_spam, p_spam)
	prediction_ham = p_ham * get_email_cond_p(msg, words_ham, p_ham)

	print("Probability of Spam: {}".format(prediction_spam))
	print("Probability of Ham: {}".format(prediction_ham))
	if prediction_spam > prediction_ham: 
		print ("It's SPAM!")
	else: 
		print("False Alarm, it's delicious Ham!")



def input_loop(): 
	print("Exit the program by typing: quit")

	isContinue = True
	while isContinue: 
		user_input = input("Enter an SMS message to determine SPAM or HAM: ")
		if user_input == 'quit': 
			break
		get_prob_predictions(user_input, words_spam, words_ham, p_spam, p_ham)



if __name__ == '__main__':
	data = [line.strip() for line in read_file(SPAM_FILE)] 
	
	p_spam, p_ham, words_spam, words_ham, pos_count, neg_count = train_spam(data)

	input_loop()
	


