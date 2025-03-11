
        # Lesson 39 - Highest Score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# total_exam_score = sum(student_scores)
# # print(total_exam_score)

# sum = 0
# for score in student_scores:          # replicates sum() functionality
#     sum += score

# print(sum)

# mini challenge
# replicate max() functionality - picking out the largest number of a given set
# print(max(student_scores))

max = 0
for score in student_scores:
#     print(str(score) + " " + str(max))        # just for testing
    if score > max:
        max = score
#     print(str(score) + " " + str(max))        # just for testing

print(max)