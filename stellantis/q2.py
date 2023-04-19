def findSuspiciousIds (log, threshold):
    user_counts = {}
    for row in log:
        sender, receiver, _ = row.split()
        if sender == receiver:
            count = 0 if not user_counts.get(sender) else user_counts.get(sender)
            user_counts[sender] = count+1
        else:
            sender_count = 0 if not user_counts.get(sender) else user_counts.get(sender)
            user_counts[sender] = sender_count+1
            receiver_count = 0 if not user_counts.get(receiver) else user_counts.get(receiver)
            user_counts[receiver] = receiver_count+1
    suspicious = []
    for i, j in user_counts.items():
        if j >= threshold:
            suspicious.append(i)
    suspicious.sort()
    return suspicious


if __name__ == '__main__':
    logs = ["12 99 200", "88 88 300", "99 32 100", "3 12 15"]
    print(findSuspiciousIds(logs, 3))
