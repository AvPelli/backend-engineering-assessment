from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question, Answer, Participant

class Command(BaseCommand):
    help = 'Create a funny quiz'

    def handle(self, *args, **kwargs):
        # generate 2 dummy quizzes
        n = 2
        for i in range(1,n+1):

            if Quiz.objects.filter(title='The Ultimate Fun Quiz' + str(i)).exists():
                self.stdout.write(self.style.WARNING('Quiz already exists. No new quiz created.'))
            else:
                quiz = Quiz.objects.create(title='The Ultimate Fun Quiz' + str(i), creator_id=1)  # Adjust creator_id as needed

                questions = [
                    {
                        'text': 'What is the best way to start your day?',
                        'answers': [
                            ('With a cup of coffee and a smile 😊', True),
                            ('By hitting the snooze button... again 😴', False),
                            ('Dancing to your favorite song 💃', False),
                            ('Checking your emails 📧', False),
                        ]
                    },
                    {
                        'text': 'If you could have any superpower, what would it be?',
                        'answers': [
                            ('Invisibility 🕵️‍♂️', False),
                            ('Flying like a bird 🦅', False),
                            ('Super strength 💪', False),
                            ('The ability to make anyone laugh 😂', True),
                        ]
                    },
                    {
                        'text': 'What is the most important ingredient in a sandwich?',
                        'answers': [
                            ('The bread 🍞', False),
                            ('The filling 🥪', False),
                            ('The love you put into making it ❤️', True),
                            ('The secret sauce 🥫', False),
                        ]
                    },
                    {
                        'text': 'Which animal would make the best CEO?',
                        'answers': [
                            ('A wise owl 🦉', True),
                            ('A hardworking ant 🐜', False),
                            ('A playful dolphin 🐬', False),
                            ('A lazy cat 🐱', False),
                        ]
                    },
                    {
                        'text': 'What is the best way to relax after a long day?',
                        'answers': [
                            ('Watching your favorite TV show 📺', False),
                            ('Taking a bubble bath 🛁', False),
                            ('Reading a good book 📚', False),
                            ('Eating a giant bowl of ice cream 🍨', True),
                        ]
                    },
                ]

                for q in questions:
                    question = Question.objects.create(quiz=quiz, text=q['text'])
                    for answer_text, is_correct in q['answers']:
                        Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)


                #add user as participant to this quiz
                Participant.objects.create(score=0,user_id=1,quiz_id=i)
                self.stdout.write(self.style.SUCCESS('Successfully created the quiz'))