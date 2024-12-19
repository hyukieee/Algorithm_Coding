fun main() {
    val num = readLine()!!.toInt()

    var tmp = num
    var cnt =0


    do {
        val num10 = tmp / 10
        val num1 = tmp %10
        val sum = num10 +num1

        tmp = (num1 *10) + (sum %10)

        cnt++

    }while (tmp != num)


    println(cnt)


}



