

def solution(answers):
    answer = []
    player1 = [ 1, 2, 3, 4, 5,]
    player2 = [ 2, 1, 2, 3, 2, 4, 2, 5,]
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    score = [0] * 3
    
    for i in range(len(answers)):
        if player1[i%len(player1)] == answers[i]:
            score[0] += 1
        if player2[i%len(player2)] == answers[i]:
            score[1] += 1
        if player3[i%len(player3)] == answers[i]:
            score[2] += 1
    
    highscore = max(score)

    
    for i in range(3):
        if(score[i] == highscore):
            answer.append(i+1)
            
    return answer
