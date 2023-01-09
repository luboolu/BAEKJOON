//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 2525 오븐 시계

let input1 = readLine()! //현재 시각 시 : 분
let input2 = readLine()! //요리하는데 필요한 시간(분 단위)

let startTime = input1.split(separator: " ").map({Int($0)!})
let startMinute = startTime[0] * 60 + startTime[1]

let endTime = startMinute + Int(input2)!

var endHour = endTime / 60
let endMinute = endTime % 60

if endHour >= 24 {
    endHour -= 24
}

print(endHour, endMinute)
