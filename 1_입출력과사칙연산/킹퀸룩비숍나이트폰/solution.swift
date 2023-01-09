//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 3003
let input = readLine()!

let chess = [1, 1, 2, 2, 2, 8]
let myChess = String(input).split(separator: " ").map({Int($0)!})
var answer: [Int] = []

for (i, my) in myChess.enumerated() {
    if chess[i] > my {
        answer.append(chess[i] - my)
    } else if chess[i] < my {
        answer.append(chess[i] - my)
    } else {
        answer.append(0)
    }
}

print(answer.map({String($0)}).joined(separator: " "))
