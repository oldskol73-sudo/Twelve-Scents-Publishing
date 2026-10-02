import SwiftUI

@main
struct TwelveScentsApp: App {
    var body: some Scene {
        WindowGroup {
            WebContainer()
                .ignoresSafeArea()
                .background(Color(red: 0.078, green: 0.067, blue: 0.055)) // #14110e
                .preferredColorScheme(.dark)
        }
    }
}
