export default async function backendApi () {
    try{
        const response = await fetch(``, {
            method: 'GET' // Declares right the method
        })
        const posts = await response.json()

        console.log(posts)

    } catch (err) {
        alert('The server is not responding', err)
    }
    
}