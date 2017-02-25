import sql


class Question:

    def __init__(self, question_id, quiz_id, question, a_one, a_two, a_three, good, img_url=None):
        """
        :param question_id: int (id from DB)
        :param quiz_id: int (quiz_id for which question is
        :param question: string (text of question)
        :param a_one: string (text of first answer)
        :param a_two: string (text of second answer)
        :param a_three: string (text of third answer)
        :param good: string (text of good answer)
        :param img_url: string (url to img if given)
        """
        self.question_id = question_id
        self.quiz_id = quiz_id
        self.question = question
        self.a_one = a_one
        self.a_two =a_two
        self.a_three = a_three
        self.good = good
        self.img_url = img_url


    @classmethod
    def add_question(cls, quiz_id, question, a_one, a_two, a_three, good, img_url=None):
        """"""
        query = "SELECT max(ID) FROM QUESTIONS"
        new_id = sql.query(query)[0][0] + 1
        print(new_id)
        new_question = cls(new_id, quiz_id, question, a_one, a_two, a_three, good, img_url)
        query_2 = """INSERT INTO QUESTIONS (quiz_id, question, a_one, a_two, a_three, a_good, img)
                     VALUES (?, ?, ?, ?, ?, ?, ?)"""
        params = [quiz_id, question, a_one, a_two, a_three, good, img_url]
        sql.query(query_2, params)
        return new_question

    def if_answer_correct(self, user_choice):
        if user_choice == self.good:
            return True
        return False

    @staticmethod
    def get_questions_by_id(quiz_id):
        query = "SELECT * FROM QUESTIONS WHERE quiz_id=(?)"
        ans_list = sql.query(query, [quiz_id])
        list_to_push =[]
        for ans in ans_list:
            list_to_push.append([ans['id'], ans['quiz_id'], ans['img'], ans['question'], ans['a_one'], ans['a_two'], ans['a_three'],
                                 ans['a_good']])
        print(list_to_push)
        return list_to_push

    def __str__(self):
        return '{}-{}-{}'.format(self.question_id, self.question, self.good)

"""question = 'Who is this?'
a_one = 'Pope'
a_two = 'Santa'
a_three = 'Pikachu'
good = 'Pikachu'
img = "http://cartoonbros.com/wp-content/uploads/2016/08/pikachu-6.png"
print(Question.add_question(3, question, a_one, a_two, a_three, good, img))"""
Question.get_questions_by_id(1)