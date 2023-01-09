//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 10807 개수 세기

//총 N개의 정수가 주어졌을때, 정수 V가 몇 개인지 구하시오
let n = Int(readLine()!)!
let list = readLine()!.split(separator: " ").compactMap({Int($0)}).sorted(by: <)
let v = Int(readLine()!)!

print(list.filter({$0 == v}).count)
