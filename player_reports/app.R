library(shiny)

ui <- fluidPage(
  titlePanel("Player Reports"),
  
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    sidebarPanel(
      h3("Roster"),
      
      selectInput("player", 
                  label = "Select a player", 
                  choices = list("Select a player",
                    "Catchers" = c("#5 Patrick Bailey", 
                                   "#12 Brad Deb",
                                   "#23 Jack Conley", 
                                   "#24 Brady Gulakowski"),
                    "In Fielders" = c("#2 David Vazquez", 
                                      "#3 Devonte Brown",
                                      "#7 Stephen Pitarra", 
                                      "#8 Will Wilson",
                                      "#16 Shane Shepard",
                                      "#17 Dillon Cooper",
                                      "#18 Evan Edwards",
                                      "#32 Steven Oakley",
                                      "#42 J.T. Jarrett"),
                    "Out Fielders" = c("#1 Terrell Tatum", 
                                       "#6 Brett Kinneman",
                                       "#11 Lawson McArthur", 
                                       "#13 Brock Deatherage",
                                       "#15 Josh McLain",
                                       "#31 Hunter Baker"),
                    "Left Handed Pitchers" = c("#10 David Harrison", 
                                               "#28 James Ferguson",
                                               "#34 Evan Justice", 
                                               "#38 Brian Brown",
                                               "#43 Connor Centala",
                                               "#44 Kent Klyman",
                                               "#46 Nick Swiney",
                                               "#47 Cole Hooper",
                                               "#51 Josh Jimenez"),
                    "Right Handed Pitchers" = c("#19 Dalton Feeney", 
                                                "#20 Austin Staley",
                                                "#26 Michael Bienlien", 
                                                "#27 James Vaughan",
                                                "#29 Reid Johnston",
                                                "#30 Mathieu Gauthier",
                                                "#33 Johnny Piedmonte",
                                                "#35 Cameron Cotter",
                                                "#39 Nolan Clenney",
                                                "#41 Joe O'Donnell",
                                                "#45 Josh Pike")
                  )
      ) # end select input
    ), # end sidebar panel
    mainPanel(
      h3("Player, Position", label="player"),
      selectInput("game", 
                  label = "Show stats for:",
                  choices = list("Last Game", 
                                 "Last 3 Games",
                                 "Last 7 Games", 
                                 "Entire Season"),
                  selected = "Last Game"
      ), #end selectInput
      fluidRow(
        column(4,
           h4("Row 1, Column 1"),
           br()
        ), # end row 1 column 1
        column(4,
           h4("Row 1, Column 2"),
           br()
        ) # end row 1 column 2
      ), #end fluid row
      fluidRow(
        column(4,
           h4("Row 2, Column 1"),
           br()
        ), # end row 2, column 1
        column(4,
           h4("Row 2, Column 2"),
           br()
        ) # end row 2, column 2
      ) # end fluid row
    ) # end main panel
  )
)

server <- function(input, output, session) {
  session$onSessionEnded(stopApp)
}

shinyApp(ui = ui, server = server)