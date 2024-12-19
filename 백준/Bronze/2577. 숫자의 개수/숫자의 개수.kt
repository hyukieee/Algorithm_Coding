fun main (){
    val a = readln().toInt()
    val b = readln().toInt()
    val c = readln().toInt()

    var result = a*b*c

    val array: Array<Int> = arrayOf(0,0,0,0,0,0,0,0,0,0)

    while(result > 0){
        val idx = result % 10
        array[idx] += 1

        result /= 10
    }

    for(i in 0..9){
        println(array[i])
    }
}