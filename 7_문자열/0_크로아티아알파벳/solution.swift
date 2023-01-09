//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 2941 크로아티아 알파벳

var input = readLine()!
let croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

croatia.forEach { c in
//replacingOccurrences는 Foundation의 StringProtocol에 존재하므로 사용하기 위해선 import Foundation이 필수
input = input.replacingOccurrences(of: c, with: "!")
}

print(Array(input).count)
