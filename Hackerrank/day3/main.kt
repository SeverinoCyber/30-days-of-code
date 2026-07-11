import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*



fun main(args: Array<String>) {
    val N = readLine()!!.trim().toInt()
    if (N % 2 == 1){
        println("Weird")
    } else{
        if(N >= 2 && N <= 5){
            println("Not Weird")
        } else if(N >= 6 && N <= 20){
            println("Weird")
        } else if(N >20){
            println("Not Weird")
        }
    }
}
