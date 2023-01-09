//
//  solution.swift
//  Test
//
//  Created by 김진영 on 2023/01/09.
//

import Foundation

//MARK: 1157 단어공부

//주어진 단어에서 가장 많이 사용된 알파벳을 구하시오(단, 대소문자 구분하지 않고 답이 여러개 존재하는 경우에는 ?를 출력)
let input = Array(readLine()!).sorted().map({$0.uppercased()})
let setInput = Array(Set(input)).sorted()
var count = Array(repeating: 0, count: setInput.count)

for (i, s) in setInput.enumerated() {
    count[i] = input.filter({$0 == s}).count
}

// if Set(count).count != count.count
// 이런식으로 ? 가 출력되는 조건을 걸면 안되는 이유..
// 같은 수 만큼 중복해서 나온 문자가 가장 많이 사용된 알파벳이 아닌 경우!
// 이러한 경우를 제대로 구분하지 못하는 조건문이다.
if count.filter({$0 == count.max()!}).count != 1 {
    print("?")
} else {
    print(setInput[count.firstIndex(of: count.sorted(by: >).first!)!])
}

