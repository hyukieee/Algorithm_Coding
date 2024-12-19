fun main() {
    val grade = readln()

    var alpha:Double= 0.0
    var plma:Double=0.0

    if (grade[0] == 'F'){
        println("0.0")
        return

    }
    alpha = when  (grade[0]){
        'A' -> 4.0
        'B' -> 3.0
        'C' -> 2.0
        'D' -> 1.0
        'F' -> 0.0

        else -> 0.0
    }

    plma = when  (grade[1]){
        '+'-> 0.3
        '-'-> -0.3
        '0'-> 0.0
        else -> 0.0
    }

    println(alpha+ plma)
}