
class Utils{

    numberToString(number){
        return parseFloat(String(number).replace(/\./g, '').replace(/\,/g, '.'))
    }

}