//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 25304 영수증

//영수증 각 항목의 합계와 총 금액이 일치하는지 확인
let totalCount = Int(readLine()!)!
let n = Int(readLine()!)!
var myTotalCount = 0

for i in (0..<n) {
    let input = readLine()!.split(separator: " ")
    myTotalCount += Int(input[0])! * Int(input[1])!
}

if myTotalCount != totalCount {
    print("No")
} else {
    print("Yes")
}

