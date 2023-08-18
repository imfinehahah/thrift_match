namespace cpp match_service

struct User {
    1: i32 id,
    2: string name,
    3: i32 score
}

service Match {
    // 添加用户信息
    i32 add_user(1: User user, 2: string info),

    // 删除用户信息
    i32 remove_user(1: User user, 2: string info),
}

