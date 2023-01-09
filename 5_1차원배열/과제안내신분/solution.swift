//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 5597 과제 안 내신 분..?

//학생 30명 중 28명이 과제를 제출함, 그 중 안낸 2명의 출석번호를 구하시오
var students = Array(1...30)

for _ in 0..<28 {
    let input = Int(readLine()!)!
    students.remove(at: students.firstIndex(where: {$0 == input})!)
}

print(students[0])
print(students[1])

