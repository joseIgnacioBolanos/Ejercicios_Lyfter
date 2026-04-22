
def get_average_scores(scores):
    return ((scores['spanish_score']+ scores['science_score'] + scores['history_score'] ) / 3)

def is_student_exempt(scores):
    return scores["average_score"] > 70

students= [  
 {
    'name': 'Ignacio',
  "spanish_score": 75,
	"science_score": 15,
  "history_score": 54,
},
 {
     'name': 'Pablo',
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
},
 {
     'name': 'Allan',
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}
]

# Averages
for student in students:
    student["average_score"] = get_average_scores(student)
    student["is_exempted"] = student["average_score"] > 70
    print(student)


