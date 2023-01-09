//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 2480 주사위 세개
//주사위 3개의 결과에 따라 상금을 받음
//같은눈 3개 = 10,000 + (같은 눈) * 1,000 원
//같은눈 2개 = 1,000 + (같은 눈) * 100 원
//모두 다른 눈 = (가장 큰 눈) * 100 원
let input = readLine()!
let dice = input.split(separator: " ").sorted(by: <) //오름차순 정렬
let diceSet = Set(dice)
var score = 1 //중복 횟수
var diceResult = dice[0] //중복으로 나온 주사위 눈 숫자
var result = 0 //상금

if diceSet.count == 1 {
    result = 10000 + (Int(dice[0])!) * 1000
} else if diceSet.count == 2 {
    var duplicte = 0
    dice.forEach({ d in
        if dice.filter({$0 == d}).count == 2 {
            duplicte = Int(d)!
        }
    })
    
    result = 1000 + (duplicte) * 100
} else if diceSet.count == 3 {
    result = (Int(dice[2])!) * 100
}
print(result)
