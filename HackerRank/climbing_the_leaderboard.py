def climbing_leader_board(ranked, player):
    # Time limit exceeded
    # final = []
    # for score in player:
    #     ranked.append(score)
    #     rank_set_sort = sorted(set(ranked), reverse=True)
    #     for j, score_rank in enumerate(rank_set_sort):
    #         if score == score_rank:
    #             final.append(j + 1)
    # print(final)

    # final = []
    # rank_set_sort = sorted(set(ranked), reverse=True)
    # for score in player:
    #     if score > rank_set_sort[0]:
    #         rank_set_sort.insert(0, score)
    #         final.append(1)
    #     elif score < rank_set_sort[-1]:
    #         rank_set_sort.append(score)
    #         final.append(len(rank_set_sort))
    #     else:
    #         for j in range(len(rank_set_sort)):
    #             if rank_set_sort[j] == score:
    #                 final.append(j+1)
    #                 break
    #             elif rank_set_sort[j] < score:
    #                 rank_set_sort.insert(j, score)
    #                 final.append(j + 1)
    #                 break
    #
    # print(final)
    rank_sort = [ranked[0]]
    final = []
    current = rank_sort[0]
    for i in ranked:
        if i != current:
            rank_sort.append(i)
            current = i

    for score in player:
        if score < rank_sort[-1]:
            rank_sort.append(score)
            final.append(len(rank_sort))
        elif score > rank_sort[0]:
            rank_sort.insert(0, score)
            final.append(1)
        else:
            first = 0
            last = len(rank_sort) - 1

            if first > last:
                if rank_sort[first] < score:
                    rank_sort.insert(first,score)
                    final.append(first + 1)
                else:
                    rank_sort.insert(first+1,score)
                    final.append(first+1+1)

            while first <= last:
                mid = (first + last) // 2
                if rank_sort[mid] < score:
                    last = mid - 1
                    if first == last:
                        if rank_sort[first] < score:
                            rank_sort.insert(first, score)
                            final.append(first + 1)
                            break
                        else:
                            rank_sort.insert(first + 1, score)
                            final.append(first + 1 + 1)
                            break
                elif rank_sort[mid] > score:
                    first = mid + 1
                    if first == last:
                        if rank_sort[first] < score:
                            rank_sort.insert(first, score)
                            final.append(first + 1)
                            break
                        else:
                            rank_sort.insert(first + 1, score)
                            final.append(first + 1 + 1)
                            break
                else:
                    final.append(mid + 1)
                    break
    print(final)

    # final = []
    # rank_set_sort = sorted(set(ranked), reverse=True)
    # for score in player:
    #     if score > rank_set_sort[0]:
    #         rank_set_sort.insert(0, score)
    #         final.append(1)
    #     elif score < rank_set_sort[-1]:
    #         rank_set_sort.append(score)
    #         final.append(len(rank_set_sort))
    #     else:
    #         first = 0
    #         last = len(rank_set_sort)
    #         while first < last:
    #             mid = (first + last) // 2
    #             if rank_set_sort[mid] == score:
    #                 final.append(mid+1)
    #                 break
    #             elif rank_set_sort[j] < score:
    #                 rank_set_sort.insert(j, score)
    #                 final.append(j + 1)
    #                 break
    #
    # print(final)


if __name__ == '__main__':
    climbing_leader_board([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    climbing_leader_board([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])